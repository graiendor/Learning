#include "../Headers/MEM_agent.hpp"

namespace s21 {

void MEM_agent::ram_load_average_update() {
  while (!this->stop_signal) {
    std::ifstream mem{"/proc/meminfo"};
    double available{};
    std::string skip{};
    if (mem.is_open()) {
      mem >> skip >> this->ram_total;
      mem >> skip >> skip >> skip >> skip >> skip >> available;
      this->ram_slices.push_back(available);
      mem.close();
    }
    std::this_thread::sleep_for(std::chrono::seconds(1));
  }
}

void MEM_agent::update() { 
  // Вычисляем среднее арифметическое всех записанных срезов оперативки.
  if (!this->ram_slices.empty()) {
    this->ram_load =
        std::reduce(this->ram_slices.begin(), this->ram_slices.end());
    this->ram_load /= this->rate;
    ram_slices.clear();
    this->ram_load =
        ((this->ram_total - this->ram_load) / this->ram_total) * 100;
  }
  this->ram_total /= 1024;

  // Структура, в которой хранится вся инфа о блоках (диска) системы.
  struct statvfs stat;
  statvfs("/", &stat);
  this->disk_usage = stat.f_blocks - stat.f_bfree;
  this->disk_usage /= stat.f_blocks;
  this->disk_usage *= 100;
  /* bsize = 4096 на моем линуксе, далее мы рассчитываем количество собственной
  байтов, и делим на 1024, чтобы получить мегабайты из байтов */
  // this->disk_usage = (((this->disk_usage * stat.f_bsize) / 1024) / 1024);

  disk_stats(stat.f_bsize);
  // std::cout << "RAM_total: " << this->ram_total << std::endl;
  std::cout << "RAM_load(%): " << this->ram_load << std::endl;
  std::cout << "Disk_usage(%): " << this->disk_usage << std::endl;
  std::cout << "IO: " << this->io_operations << std::endl;
  std::cout << "PUT: " << this->disk_throughput << std::endl;
  std::this_thread::sleep_for(std::chrono::seconds(this->rate));
}

/*
    Full contents of diskstats are in README
    We need:
    4  reads completed successfully
    6  sectors read
    8  writes completed
    10  sectors written
    13  time spent doing I/Os (ms)
*/
void MEM_agent::disk_stats(const unsigned long &sector_size) {
  std::ifstream diskstat{"/proc/diskstats"};
  double total_io{}, total_sectors{}, total_time{};
  std::string line;
  while (std::getline(diskstat, line)) {
    double read{}, write{}, sector_read{}, sector_write{}, time{};
    sscanf(line.c_str(), "%*d %*d %*s %lf %*d %lf %*d %lf %*d %lf %*d %*d %lf",
           &read, &sector_read, &write, &sector_write, &time);
    total_io += read + write;
    total_sectors += sector_read + sector_write;
    total_time += time;
  }

  if (this->prev_io == 0) {
    this->prev_io = total_io;
    this->prev_sectors = total_sectors;
  } else {
    this->io_operations = (total_io - this->prev_io) / this->rate;
    this->prev_io = total_io;
    this->disk_throughput =
        ((((total_sectors - prev_sectors) * sector_size) / 1024) / 1024) /
        ((total_time - prev_time) / 1000);
    this->prev_sectors = total_sectors;
    this->prev_time = total_time;
  }
  diskstat.close();
}

void MEM_agent::run() {
  this->stop_signal = false;
  // std::thread t0([&] { update(); });
  std::thread t1([&] { ram_load_average_update(); });
  // t0.join();
  // t1.join();
  while (!this->stop_signal) {
    update();
  }
}

void MEM_agent::stop() { this->stop_signal = true; }

double MEM_agent::get_ram_total() { return this->ram_total; }
double MEM_agent::get_ram() { return this->ram_load; }
double MEM_agent::get_hard_volume() { return this->disk_usage; }
int MEM_agent::get_hard_ops() { return this->io_operations; }
double MEM_agent::get_hard_throughput() { return this->disk_throughput; }

}  // namespace s21

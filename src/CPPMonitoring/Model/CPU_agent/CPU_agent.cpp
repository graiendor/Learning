#include "../Headers/CPU_agent.hpp"

namespace s21 {
void CPU_agent::update() {
  // В этом файле лежит загрузка процессора, нам нужно первое значение - за 1
  // минуту.
  std::ifstream loadavg{"/proc/loadavg"};
  if (loadavg.is_open()) {
    redi::ipstream processors("lscpu | grep '^CPU(s):'");
    if (processors.is_open()) {
      loadavg >> this->cpu_load;
      std::string pr{};
      double ok{};
      processors >> pr >> ok;
      this->cpu_load /= ok;
      this->cpu_load *= 100;
      processors.close();
    }
    loadavg.close();
  }
  // В этой файле лежит статистика по процессам в системе.
  std::ifstream processes{"/proc/stat"};
  std::string word{};
  while (processes >> word) {
    if (word == "procs_running") {
      processes >> this->number_of_processes;
      break;
    }
  }
}

void CPU_agent::run() {
  this->stop_signal = false;
  while (!this->stop_signal) {
    update();
    std::cout << "CPU Load Average: " << this->cpu_load << std::endl;
    std::cout << "Total number of proccesses active: "
              << this->number_of_processes << std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(60));
  }
}

void CPU_agent::stop() { this->stop_signal = true; }

double CPU_agent::get_cpu_load() { return this->cpu_load; }

int CPU_agent::get_number_of_processes() { return this->number_of_processes; }

}  // namespace s21

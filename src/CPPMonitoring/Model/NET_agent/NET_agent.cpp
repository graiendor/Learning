#include "../Headers/NET_agent.hpp"

namespace s21 {
void NET_agent::update() {
  std::string command{"curl -Is " + this->url + " | head -1"};
  redi::ipstream curl(command);
  int code{};
  curl >> command >> code;
  if (code == 200) {
    this->availability = true;
  }

  std::ifstream net{"/proc/net/dev"};
  std::string line;
  for (int _{0}; _ < 2; _++) {
    std::getline(net, line);
  }
  double total_bytes{};
  while (std::getline(net, line)) {
    double received{}, transmitted{};
    sscanf(line.c_str(), "%*s %lf %*d %*d %*d %*d %*d %*d %*d %lf", &received,
           &transmitted);
    total_bytes += received + transmitted;
  }
  total_bytes /= 1024;
  total_bytes /= 1024;
  if (prev_bytes == 0) {
    prev_bytes = total_bytes;
  } else {
    this->inet_throughput = total_bytes - prev_bytes;
    this->inet_throughput /= rate;
    prev_bytes = total_bytes;
  }
  std::cout << "Available: " << this->availability << std::endl;
  std::cout << "Net PUT: " << this->inet_throughput << std::endl;
  std::this_thread::sleep_for(std::chrono::seconds(this->rate));
}

void NET_agent::run() {
  this->stop_signal = false;
  while (!this->stop_signal) {
    update();
  }
}

void NET_agent::stop() { this->stop_signal = true; }

int NET_agent::get_url() { return this->availability; }
double NET_agent::get_inet_throughput() { return this->inet_throughput; }
}  // namespace s21

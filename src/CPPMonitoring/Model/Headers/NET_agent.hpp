#pragma once

#include <sys/statvfs.h>

#include <chrono>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include "pstream.h"

#include "regex"

namespace s21 {
class NET_agent {
 private:
  /// URL from config.
  std::string url{"http://www.vk.com"};

  /// Shows, if the given URL is available.
  int availability{false};

  /// Measure of how fast network interfaces can transfer data.
  double inet_throughput{};

  /// Collects the info from the system.
  void update();

  /// Signal to stop running.
  bool stop_signal{true};

  /// Rate of update in seconds.
  int rate{5};

  /// Variable for throughput measurement.
  double prev_bytes{};

 public:
  /// Runs agent as infinite loop.
  void run();
  /// Sends stop signal to stop running
  void stop();

  /// Returns 1. if url is available and 0, if it is not.
  int get_url();
  /// Returns inet speed of all interfaces as MB per second.
  double get_inet_throughput();

};
}  // namespace s21

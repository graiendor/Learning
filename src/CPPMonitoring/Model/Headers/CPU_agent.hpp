#pragma once

#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <thread>

#include "pstream.h"
#include "regex"

namespace s21 {
class CPU_agent {
 private:
  /// Measure of the amount of computational work a system performs.
  double cpu_load{};

  /// Number of processes and threads created.
  int number_of_processes{};

  /// Collects the info from the system
  void update();

  /// Signal to stop running
  bool stop_signal{true};

 public:
  /// Runs agent as infinite loop
  void run();
  /// Sends stop signal to stop running
  void stop();

  double get_cpu_load();
  int get_number_of_processes();
};
}  // namespace s21

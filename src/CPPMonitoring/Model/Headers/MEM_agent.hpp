#pragma once

#include <sys/statvfs.h>

#include <chrono>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <string>
#include <thread>
#include <vector>
#include <numeric>
#include "pstream.h"

#include "regex"

namespace s21 {
class MEM_agent {
 private:
  /// Measure of the amount of total RAM installed.
  double ram_total{};

  /// Measure of the amount of RAM used.
  double ram_load{};

  /// Measure of the amount of disk space used.
  double disk_usage{};

  /// Measure of the amount of input/output operations of hard volume by second.
  int io_operations{};

  /// Measure of how fast (per second) storage can read/write data.
  double disk_throughput{};

  /// Collects the info from the system.
  void update();

  /// Collects load average of RAM
  void ram_load_average_update();

  /// Stores slices of RAM available
  std::vector<double> ram_slices{};

  /** Opens the "diskstats" file, then parses every disk info there and collects:
   * 
   * - The amount of read and write operations succesfully finished.
   * - The amount of succesfully read and written sectores.
   * - Time, spent on I/O operations(ms).
   * 
   * Then calculates IOPS (i/o operations per second) and throughput (disk speed per second).
  */
  void disk_stats(const unsigned long &sector_size);

  /// Signal to stop running.
  bool stop_signal{true};

  /// Rate of update in seconds.
  int rate{5};

  /// Values for I/O and throughput measuring.
  double prev_io{};
  double prev_sectors{};
  double prev_time{};

 public:
  /// Runs agent as infinite loop.
  void run();
  /// Sends stop signal to stop running
  void stop();

  /// Returns total ram installed as MB.
  double get_ram_total();
  /// Returns ram load as percents.
  double get_ram();
  /// Returns how much space is used as percents.
  double get_hard_volume();
  /// Returns I/O operations per second.
  int get_hard_ops();
  /// Returns disk speed per second.
  double get_hard_throughput();
};
}  // namespace s21

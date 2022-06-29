## CPU

https://www.linuxjournal.com/article/9001

    Load is the measure of the amount of computational work a system performs. The three values is the load average over a time interval. The intervals are, the last 1 minute, 5 minutes, and 15 minutes. Load average is computed as an exponential moving average. If you wish, you can take a deep dive and read Examining Load Average

#### Single Core System

    The load average value varies in range. With a single core system the value 0.83 means your CPU was at 83% capacity within the last minute. A value of 1.0 would mean your CPU is at exact capacity (100%). With the value 1.0 the system will be overloaded by adding even a little bit of additional work. A value greater than 1.0 means it's getting more than it can handle. This isn't bad, it just means that more processes are waiting for CPU time. You would see the slowness of the computer.

#### Multi-Core System

    With a multi-core system, you divide the load average by the number of cores you have. So for example, having a load average of 0.83 and having 4 cores, you would take 0.83 / 4 to get 0.2075 or (0.83 / 4) * 100 to get 20.75% capacity. With a quad-core system, if you had a load average greater than 4.0 that would indicate all cores are at 100% capacity, and any overload will result in processes waiting for CPU time.

## CONFIG

#### Config-parser

https://stackoverflow.com/questions/6892754/creating-a-simple-configuration-file-and-parser-in-c

## Memory

https://www.kernel.org/doc/Documentation/ABI/testing/procfs-diskstats
https://russianblogs.com/article/3631408833/
https://habr.com/ru/post/377757/

#### Пропускная способность

    Метрика показывающая с какой скоростью данные были записаны или прочитаны

    Для этой метрики используются колонки №3 read sectors и №5 write sectors. Значение сколько было прочитано или записано «секторов». Точно так же в zabbix сохраняем как изменение за секунду.

    Единственный ньюанс - значение в файле указанно «в попугаях-секторах», причем размер этого «сектора» фиксирован 512 байт и не зависит от реальных значений ни физического ни логического сектора устройства (проверял на нескольких устройствах с реальным размером физического сектора 4к). Так что чтобы пересчитать в байты — не забудьте умножить на 512.

#### Diskstats

		==  ===================================
		 1  major number
		 2  minor mumber
		 3  device name
		 4  reads completed successfully
		 5  reads merged
		 6  sectors read
		 7  time spent reading (ms)
		 8  writes completed
		 9  writes merged
		10  sectors written
		11  time spent writing (ms)
		12  I/Os currently in progress
		13  time spent doing I/Os (ms)
		14  weighted time spent doing I/Os (ms)
		15  discards completed successfully
		16  discards merged
		17  sectors discarded
		18  time spent discarding
		19  flush requests completed successfully
		20  time spent flushing
		==  =====================================

## NETWORK

https://unix.stackexchange.com/questions/148985/how-to-get-a-response-from-any-url#:~:text=curl%20%2DIs%20http%3A%2F%2Fwww,and%20the%20URL%20is%20reachable.&text=Thanks%20for%20sharing


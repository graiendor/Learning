#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <regex.h>
#include <unistd.h>

void string_process(FILE* html, const char* string, int* counter);
void disk_space(FILE* html);

int main() {
    char cpus[10][255] = {0};
    int read = 0;
    size_t len = 0;
    char* string = NULL;
    regex_t regex;
    regcomp(&regex, "^cpu[0-9]", REG_NEWLINE);
    int counter = {0};
    while (1) {
        FILE *stat = fopen("/proc/stat", "rb");
        // FILE *html = fopen("/home/graien/metric.html", "w");
        FILE *html = fopen("/metric/metrics.html", "w");
        while ((read = getline(&string, &len, stat)) != -1) {
            if (!regexec(&regex, string, 0, NULL, 0)) {
                string_process(html, string, &counter);
            }
        }
        fclose(stat);
        disk_space(html);
        fclose(html);
        free(string);
        sleep(3);
    }
    
    
    
    regfree(&regex);
}

void string_process(FILE* html, const char* string, int* counter) {
    double user = {0}, nice = {0}, system = {0}, idle = {0}, iowait = {0}, irq = {0}, softirq = {0};
    sscanf(string, "%*s %lf %lf %lf %lf %lf %lf %lf", &user, &nice, &system, &idle, &iowait, &irq, &softirq);
    fprintf(html, "# HELP node_cpu_seconds_total Seconds the CPUs spent in each mode.\n");
    fprintf(html, "# TYPE node_cpu_seconds_total counter\n");
    fprintf(html, "node_cpu_seconds_total_my{cpu=\"%d\",mode=\"user\"} %f\n", *counter, user);
    fprintf(html, "node_cpu_seconds_total_my{cpu=\"%d\",mode=\"nice\"} %f\n", *counter, nice);
    fprintf(html, "node_cpu_seconds_total_my{cpu=\"%d\",mode=\"system\"} %f\n", *counter, system);
    fprintf(html, "node_cpu_seconds_total_my{cpu=\"%d\",mode=\"idle\"} %f\n", *counter, idle);
    fprintf(html, "node_cpu_seconds_total_my{cpu=\"%d\",mode=\"iowait\"} %f\n", *counter, iowait);
    fprintf(html, "node_cpu_seconds_total_my{cpu=\"%d\",mode=\"irq\"} %f\n", *counter, irq);
    fprintf(html, "node_cpu_seconds_total_my{cpu=\"%d\",mode=\"softirq\"} %f\n", *counter, softirq);
}

void disk_space(FILE* html) {
    FILE* free_command = popen("/bin/free -b", "r");
    char* string = NULL;
    size_t len = {0};
    getline(&string, &len, free_command);
    getline(&string, &len, free_command);
    size_t free_bytes = {0}, total_bytes = {0};
    sscanf(string, "%*s %ld %*d %ld", &total_bytes, &free_bytes);

    fprintf(html, "# HELP node_memory_MemFree_bytes Memory information field MemFree_bytes.\n");
    fprintf(html, "# TYPE node_memory_MemFree_bytes gauge\n");
    fprintf(html, "node_memory_MemFree_bytes %ld\n", free_bytes);
    
    fprintf(html, "# HELP node_memory_MemTotal_bytes Memory information field MemTotal_bytes.\n");
    fprintf(html, "# TYPE node_memory_MemTotal_bytes gauge\n");
    fprintf(html, "node_memory_MemTotal_bytes %ld\n", total_bytes);
    free(string);
    fclose(free_command);
}

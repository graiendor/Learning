//
// Created by Emery Reva on 4/21/22.
//

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main() {
  time_t t;
  srand((unsigned)time(&t));

  struct tm tm = *localtime(&t);
  int responses[10] = {200, 201, 400, 401, 403, 404, 500, 501, 502, 503};
  char* methods[5] = {"GET", "POST", "PUT", "PATCH", "DELETE"};
  char* protocols[4] = {"HTTP/0.9", "HTTP/1.0", "HTTP/1.1", "HTTP/2.0"};
  char* sources[10] = {"/status",
                       "/list",
                       "/wp-content",
                       "/wp-admin",
                       "/explore",
                       "/search/tag/list",
                       "/app/main/posts",
                       "/posts/posts/explore",
                       "/apps/cart.jsp?appID=",
                       ""};
  char* agents[8] = {
      "Google Chrome",        "Opera",          "Safari",
      "Internet Explorer",    "Microsoft Edge", "Crawler and bot",
      "Library and net tool", "\"-\""};

  char result[500];

  int hours = {0};
  int minutes = {0};
  int seconds = {0};
  //
  int current_seconds = rand() % 200;
  for (int iter = 0; iter < 5; iter++) {
    char filename[50];
    sprintf(filename, "nginx_log_%d-%d-%d.log", tm.tm_year + 1900,
            tm.tm_mon + 1, tm.tm_mday - iter);
    FILE* file = fopen(filename, "w");
    for (int i = 0; i < (rand() % (1000 - 100 + 1)) + 100; i++) {
      sprintf(result, "%d.%d.%d.%d", rand() % 255, rand() % 255, rand() % 255,
              rand() % 255);

      sprintf(result, "%s %d", result, responses[rand() % 9]);

      sprintf(result, "%s %s", result, "graiendor");

      current_seconds += rand() % 150;
      seconds = current_seconds % 60;
      minutes = current_seconds / 60;
      hours = current_seconds / 3600;
      minutes = minutes % 60;

      sprintf(result, "%s [%d/%s/%d:%02d:%02d:%02d -0000]", result,
              tm.tm_mday - iter, "Apr", tm.tm_year + 1900, hours, minutes,
              seconds);

      sprintf(result, "%s \"%s %s %s\" 200 1043", result, methods[rand() % 5],
              sources[rand() % 9], protocols[rand() % 3]);

      sprintf(result, "%s \"%s\"", result, agents[rand() % 7]);

      fprintf(file, "%s\n", result);
    }

    fclose(file);
  }
}

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <dirent.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {  
        printf("Child PID: %d\n", getpid()); 

        struct stat file_info;
        stat("sample.txt", &file_info);
        printf("sample.txt size: %ld bytes\n", file_info.st_size);

        DIR *dir = opendir(".");  
        struct dirent *entry;
        while ((entry = readdir(dir)) != NULL) {
            printf("Found: %s\n", entry->d_name);
        }
        close(dirfd(dir)); 

        execlp("date", "date", NULL);
        exit(EXIT_FAILURE);  
    } 
    else {
        printf("Parent PID: %d\n", getpid()); 
        wait(NULL); 
        exit(EXIT_SUCCESS);
    }
}
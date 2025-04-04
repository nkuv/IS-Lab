#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/stat.h>
#include <dirent.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        perror("fork failed");
        exit(EXIT_FAILURE);
    } else if (pid == 0) {
        // Child process
        printf("Child PID: %d\n", getpid());
        
        // Using stat to get file info
        struct stat file_stat;
        if (stat("test.txt", &file_stat) == 0) {
            printf("test.txt size: %ld bytes\n", file_stat.st_size);
        } else {
            perror("stat failed");
        }
        
        // Using opendir/readdir to list directory
        DIR *dir = opendir(".");
        if (!dir) {
            perror("opendir failed");
            exit(EXIT_FAILURE);
        }
        
        struct dirent *entry;
        printf("Directory entries:\n");
        while ((entry = readdir(dir)) != NULL) {
            printf("%s\n", entry->d_name);
        }
        closedir(dir);
        
        // Close stdout and execute a command
        close(STDOUT_FILENO); // Close standard output
        printf("This won't be printed\n"); // This will fail
        
        execlp("ls", "ls", "-l", NULL); // Output suppressed due to closed stdout
        perror("exec failed"); // This will print to stderr if exec fails
        exit(EXIT_FAILURE);
    } else {
        // Parent process
        printf("Parent PID: %d\n", getpid());
        wait(NULL); // Wait for child to finish
        printf("Parent: Child process completed.\n");
        exit(EXIT_SUCCESS);
    }
}
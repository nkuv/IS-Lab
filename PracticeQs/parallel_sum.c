// Write a C program that takes an integer N as input and creates two child processes to compute the sum of numbers from 1 to N in parallel.
// First child process calculates the sum from 1 to N/2.
// Second child process calculates the sum from (N/2 + 1) to N.
// The parent process waits for both child processes to complete, retrieves their results, computes the total sum, and displays the final result.

#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <fcntl.h>

int main() {
    int n, sum1 = 0, sum2 = 0;
    printf("Enter n: ");
    scanf("%d", &n);

    int pipe1[2], pipe2[2];
    pipe(pipe1);
    pipe(pipe2);

    pid_t pid1 = fork(); 
    if (pid1 == 0) { 
        for (int i = 1; i <= n / 2; i++) sum1 += i;
        write(pipe1[1], &sum1, sizeof(sum1)); 
        close(pipe1[1]);
        return 0;
    }

    pid_t pid2 = fork();
    if (pid2 == 0) {
        for (int i = (n / 2) + 1; i <= n; i++) sum2 += i;
        write(pipe2[1], &sum2, sizeof(sum2)); 
        close(pipe2[1]);
        return 0;
    }

    close(pipe1[1]);
    close(pipe2[1]);

    read(pipe1[0], &sum1, sizeof(sum1));
    read(pipe2[0], &sum2, sizeof(sum2));

    waitpid(pid1, NULL, 0);
    waitpid(pid2, NULL, 0);

    printf("First child sum: %d\n", sum1);
    printf("Second child sum: %d\n", sum2);
    printf("Total sum: %d\n", sum1 + sum2);

    return 0;
}


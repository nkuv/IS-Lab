#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
    int n, sum1, sum2;
    printf("Enter n: ");
    scanf("%d", &n);
    
    int pipe1[2], pipe2[2];
    pipe(pipe1);
    pipe(pipe2);

    if (fork() == 0) {          // First child
        sum1 = 0;
        for (int i = 1; i <= n/2; i++) sum1 += i;
        write(pipe1[1], &sum1, sizeof(sum1));
        return 0;
    }
    
    if (fork() == 0) {          // Second child
        sum2 = 0;
        for (int i = n/2+1; i <= n; i++) sum2 += i;
        write(pipe2[1], &sum2, sizeof(sum2));
        return 0;
    }

    // Parent process
    close(pipe1[1]); 
    close(pipe2[1]);
    
    read(pipe1[0], &sum1, sizeof(sum1));
    read(pipe2[0], &sum2, sizeof(sum2));
    
    wait(NULL); 
    wait(NULL);
    
    printf("First child sum: %d\n", sum1);
    printf("Second child sum: %d\n", sum2);
    printf("Total sum: %d\n", sum1 + sum2);
    
    return 0;
}

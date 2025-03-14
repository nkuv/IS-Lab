#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#define BUFSIZE 1024

int main() {
    int src, dst;
    char src_name[100], dst_name[100];
    char buf[BUFSIZE];
    ssize_t n;

    printf("Enter source filename: ");
    scanf("%99s", src_name);
    printf("Enter target filename: ");
    scanf("%99s", dst_name);

    if ((src = open(src_name, O_RDONLY)) < 0) {
        perror("Error opening source file");
        exit(EXIT_FAILURE);
    }
    if ((dst = open(dst_name, O_WRONLY | O_CREAT | O_TRUNC, 0644)) < 0) {
        perror("Error opening target file");
        close(src);
        exit(EXIT_FAILURE);
    }

    while ((n = read(src, buf, BUFSIZE)) > 0)
        if (write(dst, buf, n) != n) {
            perror("Error writing to target file");
            close(src);
            close(dst);
            exit(EXIT_FAILURE);
        }
    if (n < 0)
        perror("Error reading from source file");

    close(src);
    close(dst);
    printf("File copied successfully!\n");
    return EXIT_SUCCESS;
}


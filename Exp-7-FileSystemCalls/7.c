// Write a C program that reads text from a file and writes it to a new file using system calls open, read, and write. 
// Do not use the standard library functions fopen or fgets.

#include<fcntl.h>
#include<unistd.h>
#include<stdio.h>

#define BUF_SIZE 1024

int main() {
    char buffer[BUF_SIZE], src_name[100], dst_name[100];

    printf("Enter source filename: ");
    scanf("%s", src_name);
    printf("Enter target filename: ");
    scanf("%s", dst_name);

    int src = open(src_name, O_RDONLY);
    int dst = open(dst_name, O_WRONLY | O_CREAT | O_TRUNC, 0644);

    ssize_t n;
    while ((n = read(src, buffer, BUF_SIZE)) > 0)
        write(dst, buffer, n);

    close(src);
    close(dst);
    
    printf("File copied successfully!\n");
    return 0;
}

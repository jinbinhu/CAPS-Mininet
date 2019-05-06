#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<errno.h>
#include<sys/types.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<netdb.h>
#include<arpa/inet.h>
#include<unistd.h>

#define DEFAULT_PORT 23456
#define DEFAULT_IP "192.168.188.133"  //IP address at receiver
#define MAXLINE 1448*8
int main(int argc, char** argv)
{
    int    socket_fd, connect_fd;
    struct sockaddr_in  servaddr;
    char    buff[MAXLINE];
    int     n;
    //Initialize Socket
    if( (socket_fd = socket(AF_INET, SOCK_STREAM, 0)) == -1 ){
        printf("create socket error: %s(errno: %d)\n",strerror(errno),errno);
        exit(0);
    }
    //Initialization 
    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = inet_addr(DEFAULT_IP);//IP address is set to INADDR_ANY,so that the system can automatically get the IP address of the machine.
    servaddr.sin_port = htons(DEFAULT_PORT);//Set the port to DEFAULT_PORT

    //Bind the local address to the created socket 
    if( bind(socket_fd, (struct sockaddr*)&servaddr, sizeof(servaddr)) == -1){
        printf("bind socket error: %s(errno: %d)\n",strerror(errno),errno);
        exit(0);
    }
    //Start listening for client connections
    if( listen(socket_fd, 10) == -1){
        printf("listen socket error: %s(errno: %d)\n",strerror(errno),errno);
        exit(0);
    }
    printf("======waiting for client's request======\n");
    while(1){
        //Blocking until there is a client connection to avoid wasting more CPU resources.
        if( (connect_fd = accept(socket_fd, (struct sockaddr*)NULL, NULL)) == -1){
            printf("accept socket error: %s(errno: %d)",strerror(errno),errno);
            continue;
        }
        //Accept data from clients
        n = recv(connect_fd, buff, MAXLINE, 0);
        buff[n] = '\0';
        printf("recv msg from client: %s\n", buff);



    }
    close(connect_fd);
    close(socket_fd);
}

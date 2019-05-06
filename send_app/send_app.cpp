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

#define SERVER_PORT 23456
#define SERVER_IP "192.168.188.133" //Ip address at the receiver
#define MAXLINE 15000

using namespace std;


char sendbuf2[1448*8];
int main()
{
    printf("hello\n");

    int sock;
    sock = socket(AF_INET,SOCK_STREAM,0);

    struct sockaddr_in servaddr;
    memset(&servaddr, 0, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(SERVER_PORT);
    servaddr.sin_addr.s_addr = inet_addr(SERVER_IP);

    if((connect(sock,(struct sockaddr*) &servaddr,sizeof(servaddr))) < 0 ){
        printf("connect error \n");
        exit(0);
    }

    //for(int i=0;i<10;i++){
        memset(sendbuf2,0x30,sizeof(sendbuf2));
        //printf("Send to server：%s\n",sendbuf[i]);
        if(send(sock, sendbuf2, strlen(sendbuf2), 0)<0){
            printf("send error \n");
            exit(0);
        }

    //}
    printf("send finished \n");
    int ret = 0;
    scanf("%d",&ret);
    close(sock);

    return 0;
}

/*
 * MultiThreadEx.c
 * 
 * Copyright 2016 raja <raja@raja-Inspiron-N5110>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <stdlib.h>
#include <unistd.h>

#define BUF_SIZE 1024
#define MAX_CLIENT 5

void *serv_con_handler(void *socket_desc);
int main(int argc, char **argv)
{
    int sock , new_socket , c , *new_sock, i;
    pthread_t sniffer_thread;
    for (i=1; i<=MAX_CLIENT; i++) {
        if( pthread_create( &sniffer_thread , NULL ,  serv_con_handler , (void*) i) < 0)
        {
            perror("A thread could not be created!");
            return 1;
        }
        sleep(3);
    }
    pthread_exit(NULL);
    return 0;
}

void *serv_con_handler(void *threadid)
{
    int threadnum = *(int*) threadid;
    int sock;
    struct sockaddr_in serv_addr;
    char send_data[BUF_SIZE],recv_data[BUF_SIZE];

    if((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        printf("Socket Creation Failed!\n");

    bzero((char *) &serv_addr, sizeof (serv_addr));

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");
    serv_addr.sin_port = htons(5000);

    if (connect(sock, (struct sockaddr *) &serv_addr, sizeof (serv_addr)) < 0) {
        printf("Failed to connect to server\n");
    }

    printf("Connected successfully client:%d\n", threadnum);
    while(1)
    {
        printf("This the the thread number %d\n", threadnum);
        fgets(send_data, BUF_SIZE , stdin);
        send(sock,send_data,strlen(send_data),0);

        if(recv(sock,recv_data,BUF_SIZE,0)==0)
            printf("Error!!!!!!!!!!");
        else
           fputs(recv_data,stdout);

        bzero(recv_data,BUF_SIZE);
        sleep(2);
    }
    close(sock);
    return 0;
}


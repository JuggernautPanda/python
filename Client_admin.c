/*
 * C.c
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


/*
    C ECHO client example using sockets
*/
#include<stdio.h> //printf
#include<string.h>    //strlen
#include<sys/socket.h>    //socket
#include<arpa/inet.h> //inet_addr
#include<string.h> 

int main(int argc, char **argv)
{
    int sock;
    struct sockaddr_in server;
    char message[1000] , server_reply[2000],uname[2000],passwd[2000];
    char concat[2000];
     
    //concatenate username and password
   // concat="\0";
    /*strcpy(concat,argv[1]); 
    strcat(concat,"\n");
    strcat(concat,argv[2]);
    strcat(concat,"\n");
    strcat(concat,argv[3]);
    strcat(concat,"\n"); */
    //Create socket
    printf("Hello! Welcome to ABC airlines admin login!\n");
    printf("User Name:");
    scanf("%s",uname);
    printf("Password:");
    scanf("%s",passwd);
    strcpy(concat,uname);
    strcat(concat,",");
    strcat(concat,passwd);
    strcat(concat,",");
    
    sock = socket(AF_INET , SOCK_STREAM , 0);
    if (sock == -1)
    {
        printf("Could not create socket");
    }
    puts("Socket created");
     
    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_family = AF_INET;
    server.sin_port = htons( 8888 );
 
    //Connect to remote server
    if (connect(sock , (struct sockaddr *)&server , sizeof(server)) < 0)
    {
        perror("connect failed. Error");
        return 1;
    }
     
    puts("Connected\n");
   
     
    //keep communicating with server
    while(1)
    {
        /*printf("The user name is %s: \n",argv[1]);*/
        /*uname = argv[0]; */
        /*printf("The password is %s: \n",argv[2]); 
        passwd=argv[1]; */
        //Send some data
        if( send(sock , concat , strlen(concat) , 0) < 0)
        {
            puts("Send failed");
            return 1;
        }
        
      
        
        //Receive a reply from the server
        /*if( recv(sock , server_reply , 2000 , 0) < 0)
        {
            puts("recv failed");
            break;
        }
         
        puts("Server reply :");
        puts(server_reply);*/
        
    }
     
    
    return 0;
}


/*
 * TCP_Client_Send.c
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


/* tcpclientSend.c */

#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>

int main(int argc, char **argv)

{

        int sock;  
        //char send_data[1024];
        char concat[2000];
        struct hostent *host;
        struct sockaddr_in server_addr; 
        
        strcpy(concat,argv[1]); 
		strcat(concat,"\n");
		strcat(concat,argv[2]);
		strcat(concat,"\n");
		strcat(concat,argv[3]);
		strcat(concat,"\n"); 

        host = gethostbyname("127.0.0.1");
		
        if ((sock = socket(AF_INET, SOCK_STREAM, 0)) == -1) {
            perror("Socket");
            exit(1);
        }

        server_addr.sin_family = AF_INET;     
        server_addr.sin_port = htons(8888);   
        server_addr.sin_addr = *((struct in_addr *)host->h_addr);
        bzero(&(server_addr.sin_zero),8); 

        if (connect(sock, (struct sockaddr *)&server_addr,
                    sizeof(struct sockaddr)) == -1) 
        {
            perror("Connect");
            exit(1);
        }

        while(1)
        { 
           //printf("\nEnter data to send: ");
           //gets(send_data);
           send(sock,concat,strlen(concat), 0);   
           close(sock);
           break;
          
        
        }   
return 0;
}



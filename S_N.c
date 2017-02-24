/*
 * S.c
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
    C socket server example, handles multiple clients using threads
    * 
    * Compile : gcc S_N.c -o S_N -lpthread -`mysql_config --cflags --libs`
*/
 
#include<stdio.h>
#include<string.h>    //strlen
#include<stdlib.h>    //strlen
#include<my_global.h>
#include<mysql.h>
#include<sys/socket.h>
#include<arpa/inet.h> //inet_addr
#include<unistd.h>    //write
#include<pthread.h> //for threading , link with lpthread
#include<string.h> 
//the thread function
void *connection_handler(void *);
 
int main(int argc, char **argv)
{
    int socket_desc , client_sock , c , *new_sock;
    struct sockaddr_in server , client;
     
    //Create socket
    socket_desc = socket(AF_INET , SOCK_STREAM , 0);
    if (socket_desc == -1)
    {
        printf("A socket could not be created.");
    }
    puts("Socket has been created");
     
    //Prepare the sockaddr_in structure
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons( 8888 );
     
    //Bind
    if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0)
    {
        //print the error message
        perror("Failed to bind. Error");
        return 1;
    }
    puts("Successfully binded");
     
    //Listen
    listen(socket_desc , 3);
     
    //Accept and incoming connection
    puts("Server is waiting for incoming connections...");
    c = sizeof(struct sockaddr_in);
     
    while( (client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c)) )
    {
        puts("Connection accepted");
         
        pthread_t sniffer_thread;
        new_sock = malloc(1);
        *new_sock = client_sock;
         
        if( pthread_create( &sniffer_thread , NULL ,  connection_handler , (void*) new_sock) < 0)
        {
            perror("A thread could not be created");
            return 1;
        }
         
        //Now join the thread , so that we dont terminate before the thread
        //pthread_join( sniffer_thread , NULL);
        puts("A handler has been assigned");
    }
     
    if (client_sock < 0)
    {
        perror("Failed to accept");
        return 1;
    }
     
    return 0;
}

void finish_with_error(MYSQL *con)
{
  fprintf(stderr, "%s\n", mysql_error(con));
  mysql_close(con);
  exit(1);        
}
 
/*
 * This will handle connection for each client
 * */
void *connection_handler(void *socket_desc)
{
    //Get the socket descriptor
    int sock = *(int*)socket_desc;
    int read_size;
    int i=0,u=0,p=0;
    int count=0;
    char *message , client_message[2000];
    char query[2000];
    char func[50],uname[100],passwd[512];
    MYSQL *con = mysql_init(NULL);
    FILE *fp;
     
     if (con == NULL)
  {
      fprintf(stderr, "mysql_init() failed\n");
      exit(1);
  }  
  
  if (mysql_real_connect(con, "localhost", "testuser", "test623", 
          "testdb", 0, NULL, 0) == NULL) 
  {
      finish_with_error(con);
  }    
     
    //Send some messages to the client
    message = "Greetings! I am your connection handler\n";
    write(sock , message , strlen(message));
     
    message = "Now type something and i shall repeat what you type \n";
    write(sock , message , strlen(message));
     
    //Receive a message from client
    read_size = recv(sock , client_message , 2000 , 0);
    
    if (read_size > 0)
    {
	  /*printf("%s\n",client_message); */
      fp = fopen("/tmp/test.csv", "w");
      fwrite(client_message, sizeof(char),read_size, fp); 
      fclose(fp); 
      strncpy(uname,client_message,5);
		
		//printf("%s,%s,%s",func,uname,passwd);
		
		strcpy(query,"SELECT Password FROM Users Where Username='");
		strcat(query,uname);
		strcat(query,"'");
		//printf("\n The query  is: %s",query);
		//strcat(query,'\0');
		if (mysql_query(con,query)) 
		{
			finish_with_error(con);
		}
  
		MYSQL_RES *result = mysql_store_result(con);
  
		if (result == NULL) 
		{
			finish_with_error(con);
		}
		
		int num_fields = mysql_num_fields(result);

		MYSQL_ROW row;
		
		while ((row = mysql_fetch_row(result))) 
			{ 
				for(int i = 0; i < num_fields; i++) 
				{ 
					printf("%s ", row[i] ? row[i] : "NULL"); 
				} 
					printf("\n"); 
			}
  
  mysql_free_result(result);
  mysql_close(con);

		}
     
    if(read_size == 0)
    {
        puts("Client disconnected");
        fflush(stdout);
    }
    else if(read_size == -1)
    {
        perror("recv failed");
    }
         
    //Free the socket pointer
    free(socket_desc);
     
    return 0;
}



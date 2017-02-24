#include <my_global.h>
#include </usr/include/mysql/mysql.h>
/* gcc ex.c -o ex `mysql_config --cflags --libs` */

int main(int argc, char **argv)
{
	printf("%s\n",argv[1]);
  printf("MySQL client version: %s\n", mysql_get_client_info());

  exit(0);
}

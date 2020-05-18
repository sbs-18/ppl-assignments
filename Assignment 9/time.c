#include <stdio.h> 
#include <stdlib.h> 
#include <unistd.h>  
#include <pthread.h> 
#include <time.h>

void *TimeThread(void *vargp) 
{ 
    time_t curtime;
    struct tm *loc_time;
    curtime = time (NULL);
    loc_time = localtime (&curtime);
    printf("%s", asctime (loc_time));    
    return NULL; 
} 
   
int main() 
{ 
    pthread_t thread_id; 
    while(1){
        pthread_create(&thread_id, NULL, TimeThread, NULL);
        sleep(1);
    } 
    pthread_join(thread_id, NULL); 
    exit(0); 
}
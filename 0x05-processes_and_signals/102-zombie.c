#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Enter an infinite loop
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - create five zombie process
 * Return: 0 Always
 */
int main(void)
{
	pid_t pid;
	int count = 0;

	while (count < 5)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID, %d\n", pid);
			sleep(1);
			count++;
		}

		else
			exit(0);
	}
	infinite_while();
	return (0);
}

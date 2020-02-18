/*
 *	 This code was developed by the Kaiserslautern High School National Technical Honor Society
 *   for use on the Moore Airborne Modular Data Acquisition Unit(MAMDAU). For usage and 
 *   instructions refer to documentation in the extracted folder.
*/

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <string>
#include <fcntl.h>
#include <errno.h>
#include <termios.h>
#include <unistd.h>
#include <fstream>
#include <time.h>
#include <signal.h>

//error handeling
extern int errno;
static volatile int keepRunning = 1;
void intHandler(int dummy) 
{
	keepRunning = 0;
}

int main() {
	signal(SIGINT, intHandler);
	time_t ntime;
	// time for the data file
	time_t mytime = time(0);
	char timestamp_buff[10] = " ";
	strftime (timestamp_buff, 10, "%H.%M.%S", localtime(&mytime));
	std::string timestamp = std::string(timestamp_buff);
	time(&ntime);
	std::string fName = std::to_string(ntime);
	// output file name
	std::ofstream file("/etc/Moore_Flight_Computer/" + fName + " data.txt");
	// open the serial connection to the pi
	int fd = open("/dev/serial0", O_RDWR | O_NONBLOCK);
	// returns error if serial connection fails
	if (fd < 0)
	{
		std::cout << strerror(errno) << std::endl;
	}
	// make the file for output
	file << timestamp << std::endl;
	// main loop
	while(keepRunning) 
	{ 
		// character buffer for serial connection
		char buffer[257];
		memset(&buffer[0], 0, 256);
		int i = read(fd, buffer, 255);
		if (i > 0) 
		{
			//write data string
			file.write(&buffer[0], i);
			file.flush();
			std::cout.write(&buffer[0], i);
		}
		// wrapping up
		file.close();
		close(fd);
	}
}
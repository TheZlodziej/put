#include <iostream>
#include <chrono>
#include <thread>

int main()
{
    int &i{*([]()
             {
                int *retval = new int(0);
                std::thread([retval]{while(true){(*retval)++;std::this_thread::sleep_for(std::chrono::seconds(1));}}).detach();
                return retval; })()};

    while (true)
    {
        std::cout << i << '\n';
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    delete &i;
    return 0;
}
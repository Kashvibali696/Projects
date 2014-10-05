#ifndef PALINDROME_H
#define PALINDROME_H

#include <iostream>
#include <cmath>
#include <cctype>

class Text {
public:
    static bool isPalindrome(std::string);
};

bool Text::isPalindrome(std::string text) {
    int len = text.length();
    if (len == 0) {
        return false;
    }

    int mid = floor(len / 2);

    for (int i = 0; i <= mid; ++i)
    {  
        if (tolower(text[i]) != tolower(text[len - 1 - i]))
            return false;
    }

    return true;
}

#endif

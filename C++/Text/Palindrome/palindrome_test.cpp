#include <boost/test/minimal.hpp>
#include "palindrome.h"

int test_main(int argc, char **argv)
{
    BOOST_CHECK(Text::isPalindrome("asd") == false);
    BOOST_CHECK(Text::isPalindrome("kajak") == true);
    BOOST_CHECK(Text::isPalindrome("") == false);
    BOOST_CHECK(Text::isPalindrome("palindrome") == false);
    BOOST_CHECK(Text::isPalindrome("mama") == false);
    BOOST_CHECK(Text::isPalindrome("Kajak") == true);

    return 0;
}
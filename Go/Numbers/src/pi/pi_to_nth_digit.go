package pi

import "math"
import "errors"

// Enter a number and have the program generate PI up to that many decimal places.
// Keep a limit to how far the program will go.
func FindPiToNthDigit(digit int) (string, error) {
	if digit <= 0 {
		return "", errors.New("Wrong argument value!")
	}

	math.Pi
}

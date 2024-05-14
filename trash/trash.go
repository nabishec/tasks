package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var in *bufio.Reader
	var out *bufio.Writer
	in = bufio.NewReader(os.Stdin)
	out = bufio.NewWriter(os.Stdout)
	defer out.Flush()

	var a string
	fmt.Fscan(in, &a)
	for i := 0; i < len(a); i++ {
		b := a[i]
		fmt.Fprintln(out, b)
	}

	fmt.Fprint(out, a)
}

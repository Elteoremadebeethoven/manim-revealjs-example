package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
	"strconv"
)

func main() {
	num := flag.Int("p", 8080, " n-port")
	flag.Parse()

	n := *num

	PORT := ":" + strconv.Itoa(n)

	fmt.Println("Running server on: " + strconv.Itoa(n))
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		http.ServeFile(w, r, r.URL.Path[1:])
	})

	http.HandleFunc("/hi", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hi")
	})

	log.Fatal(http.ListenAndServe(PORT, nil))

}

package main

import (
	"log"
	"net/http"
	"time"
)

func main() {
	client := http.Client{
		Timeout: 1 * time.Second,
	}
	if _, err := client.Get("http://localhost:8000/create"); err != nil {
		log.Fatalf("%v\n", err)
	}

	for i := 0; i < 100; i++ {
		for i := 0; i < 40; i++ {
			go func() {
				if _, err := client.Get("http://localhost:8000/insert"); err != nil {
					log.Printf("%v\n", err)
				}
			}()
			go func() {
				if _, err := client.Get("http://localhost:8000/select"); err != nil {
					log.Printf("%v\n", err)
				}
			}()
		}
		time.Sleep(time.Second * 4)
	}
}

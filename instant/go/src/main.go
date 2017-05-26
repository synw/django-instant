/*
Experimental go module that publishes events to Centrifugo from flags input
*/

package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"strings"
	"time"

	"github.com/centrifugal/gocent"
)

// Connection defines the parameters to connect to Cent.
type Connection struct {
	Host string
	Port string
	Key  string
}

// Event defines the structure of a Cent event on the channel.
type Event struct {
	Channel    string `json:"-"`
	Message    string `json:"message"`
	EventClass string `json:"event_class"`
	Data       string `json:"data"`
}

func publish(connection *Connection, event *Event) {
	url := fmt.Sprintf("%s:%s", connection.Host, connection.Port)
	e, erro := json.Marshal(event)
	if erro != nil {
		fmt.Printf("Broadcast event json error: %s", erro.Error())
		return
	}
	//fmt.Println("CHANNEL "+event.Channel+" -> SENDING EVENT: "+e)
	d := []byte(e)
	client := gocent.NewClient(url, connection.Key, 5*time.Second)
	_, err := client.Publish(event.Channel, d)
	if err != nil {
		fmt.Printf("Centrifugo client error: %s", err.Error())
		return
	}
	return
}

func main() {
	var (
		key        string
		host       string
		port       string
		channel    string
		message    string
		eventClass string
		data       string
	)

	flag.StringVar(&key, "key", "", "Key")
	flag.StringVar(&host, "host", "localhost", "Host")
	flag.StringVar(&port, "port", "8001", "Port")
	flag.StringVar(&channel, "channel", "", "Channel")
	flag.StringVar(&message, "message", "", "Message")
	flag.StringVar(&eventClass, "event_class", "Default", "Event class")
	flag.StringVar(&data, "data", "{}", "Data")
	flag.Parse()

	cleanChannel := strings.Replace(channel, "-_-", "$", -1)
	event := &Event{cleanChannel, message, eventClass, data}
	conn := &Connection{host, port, key}
	publish(conn, event)
	return
}

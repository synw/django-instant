/*
Experimental go module that broadcasts events to Centrifugo from flags input
*/

package main

import (
	"fmt"
	"time"
	"flag"
	"strings"
	"github.com/centrifugal/gocent"
	)

type Connection struct {
	Host string
    Port string
    Key string
}	
	
type Event struct {
	Channel string
    Message string
    Event_class string
    Data string
}

func broadcast(connection *Connection, event *Event) {
	url := fmt.Sprintf("%s:%s", connection.Host, connection.Port)
	e:= fmt.Sprintf("{\"message\":\"%s\", \"event_class\":\"%s\", \"data\":%s}", event.Message, event.Event_class, event.Data)
	//fmt.Println("CHANNEL "+event.Channel+" -> SENDING EVENT: "+e)
	d := []byte(e)
	client := gocent.NewClient(url, connection.Key, 5*time.Second)
	_, err := client.Publish(event.Channel, d)
	 if err != nil {
	 	fmt.Sprintf("Centrifugo client error: %s", err.Error())
	 	return
	 }
	return
}

func main() {
	var key string
	var host string
	var port string
	var channel string
	var message string
	var event_class string
	var data string
	flag.StringVar(&key, "key", "", "Key")
	flag.StringVar(&host, "host", "localhost", "Host")
	flag.StringVar(&port, "port", "8001", "Port")
	flag.StringVar(&channel, "channel", "", "Channel")
	flag.StringVar(&message, "message", "", "Message")
	flag.StringVar(&event_class, "event_class", "Default", "Event class")
	flag.StringVar(&data, "data", "{}", "Data")
	flag.Parse()
	channel_ := strings.Replace(channel, "-_-", "$", -1)
	event := &Event{channel_, message, event_class, data}
	conn := &Connection{host, port, key}
	broadcast(conn, event)
	return
}
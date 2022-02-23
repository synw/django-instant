export default class Message {
    channelName;
    msg;
    data;
    eventClass;
    site;
    bucket;
    date;
    constructor(message) {
        console.log("NEW MSG CONS", message)
        this.channelName = message.channel;
        this.site = message.site;
        this.msg = message.message === undefined ? "" : message.message;
        this.data = message.data === undefined ? {} : message.data;
        this.eventClass = message.event_class === undefined ? "" : message.event_class;
        this.bucket = message.bucket === undefined ? "" : message.bucket;
        this.date = new Date();
    }
}

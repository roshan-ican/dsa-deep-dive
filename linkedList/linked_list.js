class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class SinglyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
  }
  push(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.tail = newNode;
      this.head = newNode;
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
    }
    this.length++;
    return this;
  }
  pop() {
    if (!this.head && !this.tail) return undefined;
    var current = this.head;
    var newTail = current;
    while (current.next) {
      newTail = current;
      current = current.next;
    }
    this.tail = newTail;
    this.tail.next = null;
    this.length--;
    if (this.length === 0) {
      this.head = null;
      this.tail = null;
    }
    return current;
  }
  shift() {
    if (!this.head && !this.tail) return undefined;
    var currentHead = this.head;
    this.head.next = currentHead.next;
    this.length--;
    return currentHead;
  }
  unshift(val) {
    const newNode = new Node(val);
    if (!this.head) {
      this.head = newNode;
      this.tail = this.head;
    }
    this.head = newNode;
    this.length++;
    return this;
  }
  get(index) {
    if (index < 0 || index >= this.length) return null;
    var counter = 0;
    var current = this.head;

    while (counter !== index && current !== null) {
      current = current.next;
      counter++;
    }

    return current;
  }

  set(index, val) {
    var foundNode = this.get(index);
    if (foundNode) {
      foundNode.val = val;
      console.log(true);
      return true;
    }
    console.log(false);
    return false;
  }
  insert(index, val) {
    if (index < 0 || index > this.length) return false;
    if (index === this.length) return !!this.push(val);

    if (index === 0) return !!this.unshift(val);
    var newNode = new Node(val);
    var prev = this.get(index - 1);
    var temp = prev.next;
    newNode.next = temp;
    this.length++;
    return true;
  }
}

var list = new SinglyLinkedList();
list.push(100);
list.push(201);
list.push(250);
list.push(350);
console.log(list, "NOW");
console.log("INSERT");
list.insert(1, 12);
let current = list.head;

while (current !== null) {
  console.log(current.val);
  current = current.next;
}

var stack = [];
stack.push("google");
stack.push("instagram");
stack.push("youtube");

console.log(stack);
stack.pop();
console.log(stack);
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }
  push(val) {
    var newNode = new Node(val);
    if (!this.first) {
      this.first = newNode;
      this.last = newNode;
    } else {
      var temp = this.first;
      this.first = newNode;
      this.first.next = temp;
    }
    return ++this.size;
  }
  pop() {
    if (!this.first) {
      return null;
    }
    if (this.first === this.last) {
      this.last = null;
    }
    this.first = this.first.next;
    this.size--;
    return temp.value;
  }
  print() {
    var arr = [];
    var current = this.head;
    while (current) {
      arr.push(current.val);
      current = current.next;
    }
    console.log(arr);
  }
}

stack.push("google");
stack.push("instagram");
stack.push("youtube");

console.log(stack); // Output: Stack { first: Node { value: 'youtube', next: Node { value: 'instagram', next: [Node] } }, last: Node { value: 'google', next: [Node] }, size: 3 }

stack.pop();
console.log(stack);

class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }
  insert(val) {
    var newNode = new Node(val);
    if (this.root === null) {
      this.root = newNode;
      return this;
    } else {
      var current = this.root;
      if (val === current.val) return undefined;
      while (true) {
        if (val < current.val) {
          if (current.left === null) {
            current.left = newNode;
            return this;
          } else {
            current = current.left;
          }
        } else if (val > current.val) {
          if (current.right === null) {
            current.right = newNode;
            return this;
          } else {
            current = current.right;
          }
        }
      }
    }
  }

  // SEARCH
  find(val) {
    if (this.root === null) return false;
    var current = this.root,
      found = false;
    while (current && !found) {
      if (val < current.val) {
        current = current.left;
      } else if (val > current.val) {
        current = current.right;
      } else {
        found = true;
      }
    }
    if (!found) {
      console.log("Value not found in the tree.", val);
      return false;
    }
    console.log("Value found in the tree.", val);
    return current;
  }
  bfsSearch() {
    var node = this.root;
    var data = [];
    var queue = [];
    queue.push(node);
    while (queue.length > 0) {
      node = queue.shift();
      console.log("Visiting node:", node);
      data.push(node.value);
      if (node.left) {
        console.log("Adding left child to queue:", node);
        queue.push(node.left);
      }
      if (node.right) {
        console.log("Adding right child to queue:", node);
        queue.push(node.right);
      }
    }
    return data;
  }

  dfsPreOrderSearch() {
    var data = [];
    var current = this.root;
    function traverse(node) {
      data.push(node);
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
    }
    traverse(current);
    console.log(data, "dfsPreOrderSearch");
    return data;
  }
  dfsPostOrderSearch() {
    var data = [];
    var current = this.root;
    function traverse(node) {
      if (node.left) traverse(node.left);
      if (node.right) traverse(node.right);
      data.push(node);
    }
    traverse(current);
    console.log(data, "dfsPostOrderSearch");
    return data;
  }
  dfsInOrderSearch() {
    var data = [];
    var current = this.root;
    function traverse(node) {
      if (node.left) traverse(node.left);
      data.push(node);
      if (node.right) traverse(node.right);
    }
    traverse(current);
    console.log(data, "dfsInOrderSearch");
  }
}

function printTree(node, indent = 0, prefix = "") {
  if (node !== null) {
    console.log(" ".repeat(indent) + prefix + node.val);
    if (node.left !== null) {
      printTree(node.left, indent + 4, "L: ");
    }
    if (node.right !== null) {
      printTree(node.right, indent + 4, "R: ");
    }
  }
}

var tree = new BinarySearchTree();
tree.insert(10);
tree.insert(6);
tree.insert(15);
tree.insert(3);
tree.insert(8);
tree.insert(20);

// tree.find(10);

// var tree = new BinaryTree();

// tree.bfsSearch();

tree.dfsPreOrderSearch();
tree.dfsPostOrderSearch();
tree.dfsInOrderSearch();

console.log("Binary Search Tree:");
// printTree(tree.root);

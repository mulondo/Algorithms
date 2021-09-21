"use strict";

function setUp() {
  var n = new Node(5);
  tree = new Tree();
  tree.addNode(n);
}

function Tree() {
  this.root = null;
}

Tree.prototype.addNode = function (n) {
  if (this.root === null) {
    this.root = n;
  }
};

function Node(val) {
  this.value = val;
  this.left = null;
  this.right = null;
}
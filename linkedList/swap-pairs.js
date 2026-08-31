function swapPairsJs(head) {
    if(!head || !head.next){
        return head
    }
    const second = head.next
    head.next = swapPairsJs(second.next)
    second.next = head

    return second
}

class ListNode1 {
    constructor(val = 0, next = null) {
        this.val = val
        this.next = next
    }
}

function buildList1(values) {
    const dummy = new ListNode1()
    let tail = dummy

    for (const value of values) {
        tail.next = new ListNode1(value)
        tail = tail.next
    }

    return dummy.next
}

function listToArray1(head) {
    const values = []
    const visited = new Set()
    let current = head

    while (current) {
        if (visited.has(current)) {
            throw new Error("The returned list contains a cycle")
        }

        visited.add(current)
        values.push(current.val)
        current = current.next
    }

    return values
}

const inputValues1 = [1, 2, 3, 4]
const head = buildList1(inputValues1)
const result = swapPairsJs(head)

console.log("Input:", inputValues1)
console.log("Output:", listToArray1(result))

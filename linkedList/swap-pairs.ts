class ListNode {
    val: number
    next: ListNode | null

    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val
        this.next = next === undefined ? null : next
    }
}

function swapPairs(head: ListNode | null): ListNode | null {
    if (!head || !head.next) {
        return null
    }

    const second = head.next
    head.next = swapPairs(second.next)
    second.next = head

    return second
}

function buildList(values: number[]): ListNode | null {
    const dummy = new ListNode()
    let tail = dummy

    for (const value of values) {
        tail.next = new ListNode(value)
        tail = tail.next
    }

    return dummy.next
}

function listToArray(head: ListNode | null): number[] {
    const values: number[] = []
    let current = head

    while (current) {
        values.push(current.val)
        current = current.next
    }

    return values
}

const inputValues = [1, 2, 3, 4]
const input = buildList(inputValues)

console.log("Input:", inputValues)

try {
    const result = swapPairs(input)
    console.log("Output:", listToArray(result))
} catch (error) {
    console.error("swapPairs failed:", error)
}

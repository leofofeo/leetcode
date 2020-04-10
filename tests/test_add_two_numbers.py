from ..add_two_numbers import reverse_li, ListNode

class TestAddTwoNumbers:
    def test_linked_li_init(self):
        li_1 = ListNode(2)
        li_2 = ListNode(4)
        li_3 = ListNode(3)
        li_1.next = li_2
        li_2.next = li_3

        assert li_1.next == li_2
        assert li_2.next == li_3
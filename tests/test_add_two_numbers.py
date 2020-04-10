from ..add_two_numbers import reverse_li, ListNode, Solution

class TestAddTwoNumbers:
    def setup(self):
        self.li_1 = ListNode(2)
        self.li_2 = ListNode(4)
        self.li_3 = ListNode(3)
        self.li_1.next = self.li_2
        self.li_2.next = self.li_3

    def test_linked_li_init(self):
        assert self.li_1.next == self.li_2
        assert self.li_2.next == self.li_3
    
    def test_reverse(self):
        expected = [self.li_1.val, self.li_2.val, self.li_3.val]
        actual = reverse_li(self.li_1)

        assert expected == actual
        assert actual != [self.li_3.val, self.li_2.val, self.li_1.val]
    
    def test_add_two_numbers(self):
        li2_1 = ListNode(5)
        li2_2 = ListNode(6)
        li2_3 = ListNode(4)
        li2_1.next = li2_2
        li2_2.next = li2_3

        sol = Solution()
        ln_expected_1 = ListNode(7)
        ln_expected_2 = ListNode(0)
        ln_expected_3 = ListNode(8)
        ln_expected_1.next = ln_expected_2
        ln_expected_2.next = ln_expected_3

        ln_actual_1 =  sol.addTwoNumbers(self.li_1, li2_1)
        ln_actual_2 = ln_actual_1.next
        ln_actual_3 = ln_actual_2.next
        assert ln_actual_1 == ln_expected_1
        assert ln_actual_2 == ln_expected_2
        assert ln_actual_3 == ln_expected_3
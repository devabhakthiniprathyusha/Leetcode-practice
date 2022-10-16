class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueHash = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0]
            local = local.replace(".", "")
            uniqueHash.add(local + '@' + domain)
        return len(uniqueHash)



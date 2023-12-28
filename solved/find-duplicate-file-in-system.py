class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = {}
    
        for path in paths:
            directory, *files = path.split()
            for file in files:
                file_name, content = file.split('(')
                content = content[:-1]  # remove the closing parenthesis
                full_path = directory + '/' + file_name
                if content in content_map:
                    content_map[content].append(full_path)
                else:
                    content_map[content] = [full_path]
    
        return [group for group in content_map.values() if len(group) > 1]

        
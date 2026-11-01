def BFS(self):
        
        current_node = self.root
        queue = []
        results = []
        
        queue.append(current_node)
        
        while queue:
            
            current_node = queue.pop(0)
            results.append(current_node.value)
            
            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
                
                
        return results

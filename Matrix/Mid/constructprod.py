class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # Determine the number of rows and columns in the given grid
        num_rows, num_cols = len(grid), len(grid[0])
      
        # Initialize a product matrix with zeros, of the same dimensions as the grid
        product_matrix = [[0] * num_cols for _ in range(num_rows)]
      
        # Define the modulo value as stated in the problem
        modulo = 12345
      
        # Initialize the suffix product variable
        suffix_product = 1
      
        # Calculate suffix products (right to left, bottom to top)
        for row in range(num_rows - 1, -1, -1):
            for col in range(num_cols - 1, -1, -1):
                # Store the current suffix product in the product_matrix at [row][col]
                product_matrix[row][col] = suffix_product
                # Update the suffix product (include the current grid value)
                suffix_product = suffix_product * grid[row][col] % modulo
      
        # Initialize the prefix product variable
        prefix_product = 1
      
        # Calculate the final product matrix values using prefix products
        for row in range(num_rows):
            for col in range(num_cols):
                # Multiply the prefix product with the already stored suffix product and apply modulo
                product_matrix[row][col] = product_matrix[row][col] * prefix_product % modulo
                # Update the prefix product (include the current grid value)
                prefix_product = prefix_product * grid[row][col] % modulo
      
        # Return the final product matrix
        return product_matrix

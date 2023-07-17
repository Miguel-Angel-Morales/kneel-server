class Order():
    def __init__(self, style_id, size_id, metal_id, id):
        self.style_id = style_id
        self.size_id = size_id
        self.metal_id = metal_id
        self.id = id

new_order = Order(1, 2, 3, 14)
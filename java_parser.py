from tree_sitter_languages import get_parser

parser = get_parser("java")

def extract_chunks(java_code: str):
    tree = parser.parse(bytes(java_code, "utf-8"))
    root = tree.root_node

    chunks = []

    cursor = root.walk()
    visited_children = False

    while True:
        node = cursor.node

        if node.type in ("class_declaration", "method_declaration"):
            start, end = node.start_byte, node.end_byte
            snippet = java_code[start:end]
            chunks.append({
                "type": node.type,
                "code": snippet
            })

        if not visited_children and cursor.goto_first_child():
            visited_children = False
            continue

        if cursor.goto_next_sibling():
            visited_children = False
            continue

        if not cursor.goto_parent():
            break

        visited_children = True

    return chunks

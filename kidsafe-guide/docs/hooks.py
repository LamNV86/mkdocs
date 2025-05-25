import re
import logging

# Cấu hình logging
logging.basicConfig(
    filename='mkdocs-hooks.log',  # File log sẽ lưu ở thư mục làm việc hiện tại
    level=logging.DEBUG,  # Mức log: DEBUG để ghi đầy đủ thông tin
    format='%(asctime)s - %(levelname)s - %(message)s'  # Định dạng log
)

logging.info("Hooks file loaded successfully.")

def on_page_markdown(markdown, page, config, files):
    """
    Extracts `keywords` metadata from the Markdown file and attaches it to the page.
    """
    logging.debug(f"Processing page: {page.file.src_path}")
    try:
        # Tìm trường `keywords` trong phần frontmatter của Markdown
        match = re.search(r'^keywords:\s*(.+)$', markdown, re.MULTILINE)
        if match:
            keywords = match.group(1).strip()
            logging.debug(f"Found keywords: {keywords}")
            if not hasattr(page, 'meta'):
                page.meta = {}
            page.meta['keywords'] = keywords
        else:
            logging.warning(f"No keywords found for page: {page.file.src_path}")
    except Exception as e:
        logging.error(f"Error processing page {page.file.src_path}: {str(e)}")
    return markdown

def on_post_page(output_content, page, config):
    """
    Injects a <meta> tag for `keywords` into the rendered HTML head.
    """
    logging.debug(f"Post-processing page: {page.file.src_path}")
    try:
        if hasattr(page, 'meta') and 'keywords' in page.meta:
            keywords_meta = f'<meta name="keywords" content="{page.meta["keywords"]}">'
            logging.debug(f"Injecting meta keywords: {keywords_meta}")
            # Thêm thẻ <meta> ngay trước </head>
            output_content = re.sub(r'(?i)(</head>)', f'{keywords_meta}\\1', output_content)
        else:
            logging.warning(f"No keywords meta to inject for page: {page.file.src_path}")
    except Exception as e:
        logging.error(f"Error injecting meta keywords for page {page.file.src_path}: {str(e)}")
    return output_content

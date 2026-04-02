import json
import tiktoken

def count_tokens_in_jsonl(filepath: str, text_key: str = "text") -> int:
    """
    Counts total tokens in a JSONL file using OpenAI's standard tokenizer.
    """
    # Initialize the tokenizer (cl100k_base is used by GPT-3.5/GPT-4)
    encoding = tiktoken.get_encoding("cl100k_base")
    
    total_tokens = 0
    total_records = 0
    
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
                
            record = json.loads(line)
            
            # Extract the text you want to train on
            text = record.get(text_key, "")
            
            # Count tokens for this specific text
            tokens = len(encoding.encode(text))
            total_tokens += tokens
            total_records += 1
            
    print(f"File processed: {filepath}")
    print(f"Total records analyzed: {total_records}")
    print(f"Total Exact Tokens: {total_tokens:,}")
    
    return total_tokens

# Run the function on your train.jsonl file
train_tokens = count_tokens_in_jsonl("train.jsonl")
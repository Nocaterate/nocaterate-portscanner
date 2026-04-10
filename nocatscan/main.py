import argparse
from concurrent.futures import ThreadPoolExecutor
from .scanner import scan_port
from .utils import save_results

def main():
    parser = argparse.ArgumentParser(description="Port Scanner Pro")

    parser.add_argument("-t", "--target", required=True, help="Target IP")
    parser.add_argument("-p", "--ports", default="1-1024", help="Port range")
    parser.add_argument("-th", "--threads", type=int, default=100, help="Threads")
    parser.add_argument("-o", "--output", help="Output file")

    args = parser.parse_args()

    try:
        start_port, end_port = map(int, args.ports.split("-"))
    except:
        print("Invalid port format. Use: 1-1000")
        return

    print(f"\n[+] Target: {args.target}")
    print(f"[+] Ports: {start_port}-{end_port}")
    print(f"[+] Threads: {args.threads}\n")

    results = []

    def task(port):
        result = scan_port(args.target, port)
        if result:
            results.append(result)

    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(task, port)

    if args.output:
        save_results(results, args.output)

    print("\n[✓] Scan selesai")

if __name__ == "__main__":
    main()
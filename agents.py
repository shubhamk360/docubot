from rag_utils import get_qa_chain

class MultiAgentPipeline:
    def __init__(self, docs):
        self.retrieval_chain = get_qa_chain(docs)
        

    def run(self, query, mode="Direct Answer"):
        if mode == "Summarize + Critique":
            query = f"Summarize and critique:\n{query}"
        elif mode == "Explain like I'm 5":
            query = f"Explain like I'm 5:\n{query}"
        return self.retrieval_chain.invoke(query)["result"]

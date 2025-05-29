# assignment-ats-recruiter

Django Assignment ATS for recruiter

---

## Development Setup Instructions

### With Docker

1. **Build and start the services:**
    ```bash
    docker-compose up --build
    ```
    This will build the candidate service and start it on port 8000.

2. **Access the API:**
    - The API will be available at [http://localhost:8000/api/v1/candidates/](http://localhost:8000/api/v1/candidates/)

---

### Without Docker

1. **Install dependencies:**
    ```bash
    cd services/candidate-service
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Run migrations:**
    ```bash
    python manage.py migrate
    ```

3. **Start the server:**
    ```bash
    python manage.py runserver 0.0.0.0:8000
    ```

---

## API Routes & Usage

All endpoints are prefixed with `/api/v1/candidates/`

1. **List Candidates**  
   `GET /api/v1/candidates/`  
   Returns a list of all candidates.

2. **Create Candidate**  
   `POST /api/v1/candidates/`  
   Body:
   ```json
   {
     "name": "...",
     "age": ...,
     "gender": "...",
     "email": "...",
     "phone": "..."
   }
   ```

3. **Retrieve Candidate**  
   `GET /api/v1/candidates/<id>/`

4. **Update Candidate**  
   `PUT /api/v1/candidates/<id>/`  
   Body:
   ```json
   {
     "name": "...",
     "age": ...,
     "gender": "...",
     "email": "...",
     "phone": "..."
   }
   ```

5. **Delete Candidate**  
   `DELETE /api/v1/candidates/<id>/`

6. **Search Candidates**  
   `GET /api/v1/candidates/search/?q=<query>`  
   Returns candidates whose names match the search query, sorted by relevancy.

---

## Search Candidate API Explanation

- The search API allows searching for candidates by name, supporting partial and multi-word queries.
- **Relevancy** is defined as the number of unique words in the search query that are present in the candidate's name (case-insensitive).
- The implementation uses a single ORM query to annotate each candidate with a relevancy score and filters out those with zero relevancy. Results are sorted by relevancy (descending) and then by name.

**Edge cases handled:**
- Empty or whitespace-only queries return an empty list.
- Duplicate words in the query are deduplicated.
- Case-insensitive matching is used.
- Only candidates with at least one matching word are returned.

---

## Additional Notes

- A management command is provided to generate 10,000 dummy candidates generate with faker to test for edge cases and performance of the query:
    ```bash
    python manage.py add_dummy_candidates
    ```
- All dependencies are listed in `requirements.txt`.
- The project uses Django and Django REST Framework.
- Example Postman collection is provided in `ATS-Recruiter-assignment.postman_collection.json`.


## What could have been improved?

- **Full-Text Search:** Integrate PostgreSQL full-text search or a dedicated search engine (like Elasticsearch) for more advanced and scalable search capabilities, especially for large datasets.
- **Testing:** Expand automated test coverage for all endpoints and edge cases.
- **Performance Optimization:** Add database indexes or caching for frequently searched fields to improve query speed.
- **Error Handling:** Improve error responses and validation feedback for a better developer and user experience.



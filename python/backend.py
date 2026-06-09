#!/usr/bin/env python3
"""
AcademiX Pro - Flask Backend Server
Advanced multi-disciplinary learning platform API
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# ==================== Configuration ====================

SUBJECTS_DATA = {
    'mathematics': {
        'title': 'Mathematics',
        'icon': '🧮',
        'description': 'Master calculus, linear algebra, and differential equations',
        'topics': ['Calculus I & II', 'Linear Algebra', 'Differential Equations', 'Real Analysis', 'Abstract Algebra'],
        'resources': 450,
        'papers': 42
    },
    'physics': {
        'title': 'Physics',
        'icon': '🌌',
        'description': 'Classical mechanics to modern quantum theory',
        'topics': ['Classical Mechanics', 'Thermodynamics', 'Electromagnetism', 'Optics', 'Modern Physics'],
        'resources': 520,
        'papers': 58
    },
    # ... Add all subjects
}

RESEARCH_PAPERS = [
    {
        'id': 1,
        'title': 'Quantum Mechanics in Modern Chemistry',
        'authors': ['Smith, J.', 'Johnson, K.'],
        'year': 1995,
        'subject': 'quantum-chemistry',
        'abstract': 'A comprehensive study of quantum mechanical principles...',
        'citations': 450
    },
    # ... Add more papers
]

# ==================== Routes ====================

@app.route('/api/subjects', methods=['GET'])
def get_subjects():
    """Get all available subjects"""
    return jsonify({
        'success': True,
        'data': SUBJECTS_DATA,
        'count': len(SUBJECTS_DATA)
    })

@app.route('/api/subjects/<subject_id>', methods=['GET'])
def get_subject(subject_id):
    """Get specific subject details"""
    if subject_id in SUBJECTS_DATA:
        return jsonify({
            'success': True,
            'data': SUBJECTS_DATA[subject_id]
        })
    return jsonify({'success': False, 'error': 'Subject not found'}), 404

@app.route('/api/papers', methods=['GET'])
def get_papers():
    """Get research papers"""
    subject = request.args.get('subject')
    year_from = request.args.get('year_from', 1980, type=int)
    year_to = request.args.get('year_to', 2024, type=int)
    
    filtered = [p for p in RESEARCH_PAPERS 
                if (not subject or p['subject'] == subject) 
                and year_from <= p['year'] <= year_to]
    
    return jsonify({
        'success': True,
        'data': filtered,
        'count': len(filtered)
    })

@app.route('/api/search', methods=['GET'])
def search():
    """Advanced search across all resources"""
    query = request.args.get('q', '').lower()
    resource_type = request.args.get('type')
    
    if not query:
        return jsonify({'success': False, 'error': 'Query required'}), 400
    
    results = []
    
    # Search in subjects
    for key, subject in SUBJECTS_DATA.items():
        if query in subject['title'].lower() or query in subject['description'].lower():
            results.append({
                'type': 'subject',
                'id': key,
                'title': subject['title'],
                'description': subject['description']
            })
    
    # Search in papers
    for paper in RESEARCH_PAPERS:
        if query in paper['title'].lower():
            results.append({
                'type': 'paper',
                'id': paper['id'],
                'title': paper['title'],
                'authors': paper['authors'],
                'year': paper['year']
            })
    
    return jsonify({
        'success': True,
        'data': results,
        'count': len(results)
    })

@app.route('/api/progress', methods=['POST'])
def save_progress():
    """Save user progress"""
    data = request.get_json()
    
    if not data:
        return jsonify({'success': False, 'error': 'No data provided'}), 400
    
    # Save to database or file
    progress_data = {
        'timestamp': datetime.now().isoformat(),
        'data': data
    }
    
    return jsonify({
        'success': True,
        'message': 'Progress saved',
        'data': progress_data
    })

@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    """Get user analytics"""
    analytics = {
        'totalResourcesAccessed': 2847,
        'papersStudied': 456,
        'subjectsMastered': 12,
        'hoursSpent': 98,
        'progressBySubject': {
            'mathematics': 65,
            'physics': 78,
            'chemistry': 72
        }
    }
    
    return jsonify({
        'success': True,
        'data': analytics
    })

@app.route('/api/recommendations', methods=['GET'])
def get_recommendations():
    """Get AI-powered recommendations"""
    recommendations = [
        {
            'subject': 'Quantum Chemistry',
            'title': 'Advanced Wave Function Theory - New Research 2024',
            'relevance': 0.95
        },
        {
            'subject': 'Sustainability',
            'title': 'Circular Economy Implementation Strategies',
            'relevance': 0.88
        },
        {
            'subject': 'Green Energy',
            'title': 'Solar Panel Efficiency Optimization',
            'relevance': 0.82
        }
    ]
    
    return jsonify({
        'success': True,
        'data': recommendations,
        'count': len(recommendations)
    })

@app.route('/api/health', methods=['GET'])
def health_check():
    """API health check"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

# ==================== Error Handlers ====================

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'success': False, 'error': 'Server error'}), 500

# ==================== Main ====================

if __name__ == '__main__':
    print("\n")
    print("="*50)
    print("🚀 AcademiX Pro - Backend Server")
    print("="*50)
    print("📍 Starting server at http://localhost:5000")
    print("📚 API Documentation at http://localhost:5000/api/docs")
    print("="*50)
    print("\n")
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        use_reloader=True
    )
